Covid Screening form for openpath using Microsoft Forms, Flow, and Azure Functions.

At midnight for each day all accounts in openpath are disabled. 

Users are required to fill out a Microsoft Form.  If they answer the questions correctly their openpath account is switched from suspended to active.

Form questions:

	
	Name
	Company
	Have you had any of the following symptoms within the last 10 days?
		Fever - yes or no
		Chills - yes or no
		Cough - yes or no
		Shortness of breath/difficulty breathing - yes or no
		New loss of taste or smell - yes or no
	Have you had contact with a person known to be infected with or suspected to have Covid-19 within the last 10 days? - yes or no
	Are you subject to a quarantine or isolation order? - yes or no
	Are you fully vaccinated against covid-19? - yes or no
	
Form criteria:

Negative Screen (Cleared)

	• The individual has no symptoms, no contact to a known COVID-19 case, AND is not under an isolation or quarantine order. They can be cleared to enter the facility. An individual with contact to a known case BUT who is fully vaccinated can also be cleared to enter.

Positive Screen (Not Cleared)

	• The individual has had contact to a known COVID-19 case in the last 10 days AND is not fully vaccinated.
	• The individual has had symptoms within the last 10 days. Provide them with COVID-19-Learn about Symptoms and What to do If You are Sick (English ph.lacounty.gov/covidcare; Spanish ph.lacounty.gov/covidcuidado
	
Flow is:

	• When response is Submitted - Used to validate questions and send email notification to the submitter for an authorized entry.

Functions are:

	• disable-users.py - Used to disable all accounts except for the API user account.
	• enable-user.py - Used to enable user account after the form has been filled out.
	
	For Robert
