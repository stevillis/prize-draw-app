# Prize Draw App

This is a simple Streamlit application designed for conducting prize draws. The application allows users to input a list of names and provides functionalities to sort them into groups or randomly select names.

## Features

1. **Group Sorting**: Users can provide a list of names and the app will sort them into a specified number of groups.
2. **Name Sorting**: Users can input a list of names and the app will randomly select n names from the list.

## Requirements

To run this application, you need to have Python installed along with the required libraries. The dependencies are listed in the `requirements.txt` file.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/stevillis/prize-draw-app.git
   cd prize-draw-app
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit application, run the following command in your terminal:
```sh
streamlit run src/app.py
```

## Usage

- Input a list of names in the provided text box.
- Choose to either sort the names into groups or randomly select two names.
- The results will be displayed on the Streamlit interface and will persist between reruns.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the application.

## License

This project is licensed under the MIT License.