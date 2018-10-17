//Log Manager source file
#include "LogManager.h"
#include "Utility.h"

//System includes
#include <stdio.h>
#include <stdarg.h>

using namespace df;

//constructor
LogManager::LogManager(){
	setType("LogManager");
	p_f = NULL;
	do_flush = false;
	//startUp(); it went into the constructor for game manager
}

//destructor
LogManager::~LogManager(){
	if(LogManager::p_f != NULL)
		shutDown();
}

//get the one and only instance of the log manager
LogManager &LogManager::getInstance(){
	static LogManager log_manager;
	return log_manager;
}

//Start up the log manager(open logfile "dragonfly.log")
int LogManager::startUp(){
	Manager::startUp();
	if (&Manager::isStarted){
		LogManager::p_f = fopen("dragonfly.log", "w+");
		return 0;
	}
	else{
		return -1;
	}
	
		
	
	
}

//Shut down the log manager(close the log file)
void LogManager::shutDown(){
	fprintf(p_f, "Shutting Down Managers. \n");
	Manager::shutDown();
	fclose(LogManager::p_f);
}

//Set flush to logfile after each write
void LogManager::setFlush(bool new_do_flush){
	do_flush = new_do_flush;
}

//Writes a log with a variable number of arguments
int LogManager::writeLog(const char *fmt, ...){
	if (LogManager::p_f != NULL){
		printf("Printing log\n");
		//get time string
		Utility util;
		fprintf(p_f, "%s", util.getTimeString());
		fprintf(p_f, "Log: ");
		va_list args;
		va_start(args, fmt);
		vfprintf(p_f, fmt, args);
		va_end(args);
		fprintf(p_f, "\n");
		if (do_flush)
			fflush(p_f);
		return 0;
	}
	else{
		printf("Error writing log to file");
		return -1;
	}
	
}



