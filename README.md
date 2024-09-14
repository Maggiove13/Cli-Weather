# CLI Weather Aplication
This Python program allows users to query the weather of a specific location using the OpenWeatherMap API. You can get information such as temperature, humidity, weather description, among others, and choose the format in which the output will be displayed (JSON, text or CSV).

##Features
- Query the weather of any city through the OpenWeatherMap API.
- Option to choose the output format: JSON, TXT or CSV.
- Use of pre-commit hooks with ruff to keep the code clean and well formatted.

### Prerequisites:
- Make sure you have Python installed on your system. You can download it from python.org.

- Git Bash (if you are on Windows, to run the Bash script)

- Git for version management and pre-commit hooks

- The necessary dependencies that can be installed using: 
```
pip install -r requirements.txt.
```
- An [OpenWeatherMap](https://openweathermap.org/api "OpenWeatherMap") API key (you register and you get a free key)

###Installation:
1- Clone the repository on your local machine:
```
git clone https://github.com/usuario/repositorio.git
```
2- Create and activate a virtual environment :
To create and activate the virtual environment, simply run the run.sh file in Git Bash or any Bash-compatible terminal:
````
./run.sh
````
This script will do the following:

-It will create a virtual environment if it does not exist.
-Activate the virtual environment.
-Install the dependencies specified in requirements.txt.
-Run the application with the default parameters (Madrid as location and json as format).

3- Configure the environment variables:

Once you have obtained your API_key, create an .env file in the root folder of your project and add your OpenWeatherMap API key in the following format:
````
API_key=your_api_key
````
4- Install pre-commit in the virtual environment:

This project uses ruff as a tool to make sure that the code follows proper formatting and linting before each commit. Make sure that the pre-commit hook is configured correctly.
````
pip install pre-commit
````

4.1- Configure pre-commit hooks:

After installing pre-commit, run the following command to install the hooks configured in .pre-commit-config.yaml:
````
pre-commit install
````


### Usage
This program is run from the terminal and accepts certain arguments to customize its operation.

Query the weather for a location
To get the weather for a specific location, use the following command:
````
python main.py -location "city"
````
You can choose the format in which you want to see the results:

JSON: Structured format as JSON.
TXT: Plain text (default).
CSV: CSV format.
#####example:
````
python main.py -location "Asuncion" -format json
````
Where:

````
-location: Specifies the name of the city to query.
-format: Defines the data output format (json, txt, or csv).
````

####Error Handling
If the API key is invalid, the following message will be shown:
```
Error: La clave API no es válida. Por favor verifica tu clave e intenta de nuevo.
```

  If the location is not found:

````
Error: Ubicación no encontrada. Por favor verifica la ortografía e intenta de nuevo.
````

------------

##Project Structure
The project is divided into modules to maintain an organized code:
- api.py: Contains the functions related to the API connection.

- get_data.py: Processes the obtained data and extracts the relevant weather information.

- error_handling.py: Handles errors that may occur during data fetching or general failures.

- main.py: The entry point of the program that controls the main logic and flow.

- run.sh: Script to automate the creation of the virtual environment, installation of dependencies and execution of the application.

- .pre-commit-config.yaml: Configuration file for pre-commit hooks.

This instruction file provides the user with all the information needed to install and use the program, not including the cache part. You can customize it according to your needs and add more details if necessary.
