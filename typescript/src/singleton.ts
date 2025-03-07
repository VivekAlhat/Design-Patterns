class Logger {
  // private static instance variable
  private static instance: Logger;

  // private constructor to prevent external initialization
  private constructor() {}

  // static method to get the instance
  public static getInstance(): Logger {
    if (!Logger.instance) {
      console.log("creating new instance");
      Logger.instance = new Logger();
    }
    return Logger.instance;
  }
}

// usage
const logger1 = Logger.getInstance();
const logger2 = Logger.getInstance();

if (logger1 === logger2) {
  console.log("both are same loggers");
}
