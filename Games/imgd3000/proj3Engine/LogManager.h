#ifndef _LOG_MANAGER_H_
#define _LOGMANAGER_H_

//System includes
#include <stdio.h>

//Engine includes
#include "Manager.h"

namespace df{
	const std::string LOGFILE_NAME = "dragonfly.log";

	class LogManager : public Manager{
		private:
			LogManager(); //Private (a singleton)
			LogManager(LogManager const&); //No copying
			void operator=(LogManager const&); //No Assignment
			bool do_flush;//True if fflush after each write
			FILE *p_f;//Pointer to logfile structure

	public: 
		//if logfile is open, close it
		~LogManager();

		//Get the one and only instance of the log manager
		static LogManager &getInstance();

		//Start up the log manager (open logfile "dragonfly.log")
		int startUp();

		//Shut down the log manager (close logfile)
		void shutDown();

		//Set flush to logfile after each write
		void setFlush(bool new_do_flush = true);

		//Write to logfile, supports printf() formatting
		//Return number of bytes written, -1 if error
		int writeLog(const char *fmt, ...);

	};
} //end namespace df
#endif //_LOG_MANAGER_H_