---
title: optimizing go-neo4j concurrency patterns
date: '2019-04-30T10:22:04.706Z'
thumb_img_path: https://miro.medium.com/max/1400/1*2ZcmyheKUHMsg-tnUDsTwQ.png
excerpt: Introduction
layout: post
---
**Introduction**

Neo4j is a noSQL database which stores data in the form of graphs. Each node of the graph has a specific tag which is used to identify the type of node. Edges between two nodes specify the relationship between the two nodes. The best use case of neo4j is in the case of embedded queries, like how many friend a peer has and how many peers do each of his/her friends have.

![](/images/optimizing-go-neo4j-concurrency-patterns/1*2ZcmyheKUHMsg-tnUDsTwQ.png)

<figcaption>Graph database</figcaption>

**Getting started**

Our aim is to set up a go-neo4j ecosystem by creating an API in golang and optimize the program to minimize response time. We will be creating a sample project which revolves around creating, reading, updating and deleting events. Let us look at some of the software requirements for the project-

*   Download seabolt from [here](https://github.com/neo4j-drivers/seabolt/releases)
*   [download neo4j](https://neo4j.com/download/)
*   seabolt installation steps [here](https://github.com/neo4j-drivers/seabolt.git)
*   Start the neo4j database by clicking on start in the neo4j desktop application
*   Get the driver for neo4j

    go get github.com/neo4j/neo4j-go-driver/neo4j

**Creating appropriate data structures**

Create a directory called lib and create the following data structures in structs.go

    package events
    import "reflect"
    type Participant struct {  
    	Name               string `json:"name"`  
    	RegistrationNumber string `json:"registrationNumber"`  
    	Email              string `json:"email"`  
    	PhoneNumber        string `json:"phoneNumber"`  
    	Gender             string `json:"gender"`  
    }
    type Event struct {  
    	ClubName              string      `json:"clubName"`  
    	Name                  string      `json:"name"`  
    	ToDate                string      `json:"toDate"`  
    	FromDate              string      `json:"fromDate"`  
    	ToTime                string      `json:"toTime"`  
    	FromTime              string      `json:"fromTime"`  
    	Budget                string      `json:"budget"`  
    	Description           string      `json:"description"`  
    	Category              string      `json:"category"`  
    	Venue                 string      `json:"venue"`  
    	Attendance            string      `json:"attendance"`  
    	ExpectedParticipants  string      `json:"expectedParticipants"`  
    	FacultyCoordinator    Participant `json:"facultyCoordinator"`  
    	StudentCoordinator    Participant `json:"studentCoordinator"`  
    	GuestDetails          Guest       `json:"guest"`  
    	PROrequest            string      `json:"PROrequest"`  
    	CampusEngineerRequest string      `json:"campusEngineerRequest"`  
    	Duration              string      `json:"duration"`  
    	MainSponsor           Participant `json:"mainSponsor"`  
    }
    // To get embedded JSON fields  
    func (v Event) GetField(field string, value string) string {  
    	r := reflect.ValueOf(v)  
    	f := reflect.Indirect(r).FieldByName(field)  
    	return f.FieldByName(value).String()  
    }

**Creating and connecting to the database instance**

First we need to listen along a specific port using the net/http module of golang

    package main
    import (  
    	"log"  
    	"net/http"  
    	"text/template"  
            "github.com/neo4j/neo4j-go-driver/neo4j"  
    )
    func main() {  
    	// connect to database  
    	session, driver, err := ConnectToDB()  
    	if err != nil {  
    		log.Fatalln("Error connecting to Database")  
    		log.Fatalln(err)  
    	}  
    	log.Println("Connected to Neo4j")  
    	// Close driver and session after func ends  
    	defer driver.Close()  
    	defer session.Close()
     // pass the session to the model layer  
    	events.SetDB(session)
     // populate templates  
    	controller.Startup()
     // listen on specified port  
    	log.Println("Starting to listen..")  
    	log.Fatal(http.ListenAndServe(":3000", nil))  
    }

Then we move on to a function which allows us to connect to the database

    func ConnectToDB() (neo4j.Session, neo4j.Driver, error) {
     // define driver, session and result vars  
    	var (  
    		driver  neo4j.Driver  
    		session neo4j.Session  
    		err     error  
    	)
     // initialize driver to connect to localhost with ID and password  
    	if driver, err = neo4j.NewDriver("bolt://localhost:7687", neo4j.BasicAuth("angad", "angad", "")); err != nil {  
    		return nil, nil, err  
    	}
     // Open a new session with write access  
    	if session, err = driver.Session(neo4j.AccessModeWrite); err != nil {  
    		return nil, nil, err  
    	}  
    	return session, driver, nil  
    }

We have created a go-neo4j ecosystem. Now we move further to create the API endpoints for sending and receiving data as well as the model layer of the application to speak to loq level database interface.

**Creating the controller layer**

This layer holds the API endpoints for the application program. Our files are defined as simple modules with **eventCRUD.go** being the file with all the endpoints  
and **router.go** holding a function to startup all the routes. Both of these files are under **/controller** directory.

**eventCRUD.go**

Here we have defined some end points which we need to implement in our API

    package controller
    import (  
    	"encoding/json"  
    	"log"  
    	"net/http"  
    	"../model"  
    )
    // Handler function for setting up endpoints  
    func eventCRUDHandler() {  
    	http.HandleFunc("/api/v1/event/create", createEvent)  
    }

**router.go**

    package controller
    // This will be called in function main for setting up routes  
    func Startup() {  
    	eventCRUDHandler()  
    }

Our API is now up and running. We just need to define the functions that we would like to perform when a call is made. But before that let us look at the low level database functions we have to implement.

**Implementing the model layer**

model layer includes **eventCreate.go**, **eventRead.go**, **eventUpdateAndDelete.go**, in the **/model** directory

**eventCreate.go**

Create participant function creates a participant node. For optimizing the transaction we have used **mutex locks**. Mutex locks use semaphores to implement mutual exclusion among the transactions in the critical section of the algorithm. The rest of the algorithm runs concurrently.

    package model
    import (  
    	"log"  
    	"sync"  
    	events "../lib"  
    )
    func CreateParticipant(e Event, label string, c chan error, mutex *sync.Mutex) {
     if e.GetField(label, "Email") == "" {  
    		c <- nil  
    		return  
    	}
    // beginning of the critical section  
    	mutex.Lock()  
    	result, err := Session.Run(`MATCH(a:EVENT) WHERE a.name=$EventName
    // low level database functions  
    	CREATE (n:INCHARGE {name:$name, registrationNumber:$registrationNumber,  
    		email:$email, phoneNumber:$phoneNumber, gender: $gender})<-[:`+label+`]-(a) `, map[string]interface{}{  
    		"EventName":          e.Name,  
    		"name":               e.GetField(label, "Name"),  
    		"registrationNumber": e.GetField(label, "RegistrationNumber"),  
    		"email":              e.GetField(label, "Email"),  
    		"phoneNumber":        e.GetField(label, "PhoneNumber"),  
    		"gender":             e.GetField(label, "Gender"),  
    	})  
    	if err != nil {  
    		c <- err  
    		return  
    	}
    // critical section ends  
    	mutex.Unlock()
     if err = result.Err(); err != nil {  
    		c <- err  
    		return  
    	}  
    	log.Printf("Created %s node", label)  
    	c <- nil  
    	return  
    }

Now we can use this function to create our own event in eventCreate.go

    func CreateEvent(e events.Event, ce chan error) {  
    	c := make(chan error)  
    	  
       // creating an event  
    	result, err := events.Session.Run(`CREATE (n:EVENT {name:$name, clubName:$clubName, toDate:$toDate,   
    		fromDate: $fromDate, toTime:$toTime, fromTime:$fromTime, budget:$budget,   
    		description:$description, category:$category, venue:$venue, attendance:$attendance,   
    		expectedParticipants:$expectedParticipants, PROrequest:$PROrequest,   
    		campusEngineerRequest:$campusEngineerRequest, duration:$duration})   
    		RETURN n.name`, map[string]interface{}{
     "name":                  e.Name,  
    		"clubName":              e.ClubName,  
    		"toDate":                e.ToDate,  
    		"fromDate":              e.FromDate,  
    		"toTime":                e.ToTime,  
    		"fromTime":              e.FromTime,  
    		"budget":                e.Budget,  
    		"description":           e.Description,  
    		"category":              e.Category,  
    		"venue":                 e.Venue,  
    		"PROrequest":            e.PROrequest,  
    		"campusEngineerRequest": e.CampusEngineerRequest,  
    		"duration":              e.Duration,  
    		"attendance":            e.Attendance,  
    		"expectedParticipants":  e.ExpectedParticipants,  
    	})  
    	if err != nil {  
    		ce <- err  
    		return  
    	}
     result.Next()  
    	log.Println(result.Record().GetByIndex(0).(string))
     if err = result.Err(); err != nil {  
    		ce <- err  
    		return  
    	}
     // CREATE STUDENT COORDINATOR, FACULTY COORDINATOR, AND SPONSOR NODES WHENEVER AN EVENT IS CREATED  
    	var mutex = &sync.Mutex{}  
    	go events.CreateParticipant(e, "StudentCoordinator", c, mutex)  
    	go events.CreateParticipant(e, "FacultyCoordinator", c, mutex)  
    	go events.CreateParticipant(e, "MainSponsor", c, mutex)
     err1, err2, err3 := <-c, <-c, <-c
     switch {  
    	case err1 != nil:  
    		ce <- err1  
    		return  
    	case err2 != nil:  
    		ce <- err2  
    		return  
    	case err3 != nil:  
    		ce <- err3  
    		return  
    	}
     log.Println("Created Event node")  
    	ce <- nil  
    	return  
    }

**Implementing the endpoint for creating the event**

In **eventCRUD.go**, the following function can be added for implementing the endpoint

    func createEvent(w http.ResponseWriter, r *http.Request) {  
    	if r.Method != http.MethodPost {  
    		w.WriteHeader(http.StatusMethodNotAllowed)  
    		return  
    	}  
    	var data events.Event  
    	err := json.NewDecoder(r.Body).Decode(&data)  
    	if err != nil {  
    		log.Println(err)  
    	}
     ce := make(chan error)
    // goroutine for invoking the model layer event create function   
    	go model.CreateEvent(data, ce)
     if err = <-ce; err != nil {  
    		log.Println(err)  
    		json.NewEncoder(w).Encode(struct {  
    			Status  bool   `json:"status"`  
    			Message string `json:"message"`  
    		}{false, "some error occurreed"})  
    		return  
    	}
     json.NewEncoder(w).Encode(struct {  
    		Status  bool   `json:"status"`  
    		Message string `json:"message"`  
    	}{true, "new node created successfully"})  
    }

Thus we created an event successfully. Now we can open the neo4j desktop application to view what the data looks like! To run the project just write **go run main.go** on your terminal.

**Result**

You might have seen that we have used mutex locks while quering the database. This is because we want all of the queries to be atomic and not interfere with each other. Thus we have devised a way of querying the database in parallel without any data integrity repercussions.

**Conclusion**

Creating a go-neo4j ecosystem is easier than ever. With new drivers like **seabolt** running the show. Optimizing it though requires a certain amount of low level programming including mutex locks and semaphores. The key is optimizing concurrency patterns in such a way that the critical section falls inside a mutex lock and the non-critical section gets executed in parallel.
