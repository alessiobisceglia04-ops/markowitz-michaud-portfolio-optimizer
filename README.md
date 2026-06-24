Markowitz–Michaud Portfolio Optimizer

A Python desktop application for portfolio optimization using the traditional Markowitz efficient frontier and Michaud resampling.

The application allows users to import financial data from an Excel workbook, generate optimized portfolios and export the resulting asset allocations back to Excel.

Project Overview

This project was developed to apply portfolio management theory through a practical Python application.

The optimizer combines:

* Markowitz mean-variance optimization
* Efficient frontier generation
* Michaud resampling
* Portfolio allocation analysis
* Excel import and export

The application currently supports portfolios containing up to 18 assets.

Main Features

* Import historical asset data from Excel
* Import manually estimated expected returns
* Calculate the variance-covariance matrix
* Generate the Markowitz efficient frontier
* Run 500 Michaud resampling simulations
* Calculate portfolio weights
* Display portfolio results
* Export allocations and analytics to Excel

Technologies Used

* Python
* pandas
* NumPy
* SciPy
* openpyxl
* matplotlib
* CustomTkinter

Project Structure

markowitz-michaud-portfolio-optimizer/
├── app.py
├── optimizer.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
├── screenshots/
└── sample_data/

app.py

Contains the graphical user interface and allows the user to:

* select an Excel workbook;
* start the optimization;
* monitor the execution;
* save the generated results.

optimizer.py

Contains the financial calculations, including:

* expected returns;
* covariance matrix calculation;
* Markowitz optimization;
* efficient frontier generation;
* Michaud resampling;
* Excel export.

sample_data/

This folder will contain a compatible sample Excel template.

The Excel template is currently being redesigned and will be added in a future update.

Requirements

Before running the application, make sure Python 3 is installed.

The required Python libraries are listed in:

requirements.txt

Installation

1. Clone the repository

Open the Terminal and run:

git clone https://github.com/YOUR-USERNAME/markowitz-michaud-portfolio-optimizer.git

Replace YOUR-USERNAME with your GitHub username.

2. Enter the project folder

cd markowitz-michaud-portfolio-optimizer

3. Create a virtual environment

On macOS or Linux:

python3 -m venv .venv
source .venv/bin/activate

On Windows:

python -m venv .venv
.venv\Scripts\activate

4. Install the required libraries

pip install -r requirements.txt

Running the Application

Start the desktop interface with:

python3 app.py

On some systems, the command may be:

python app.py

The application window should open automatically.

Excel Input File

The optimizer requires an Excel workbook with a predefined structure.

The workbook includes sections for:

* historical asset values;
* expected returns;
* portfolio results;
* Michaud resampling results.

The sample workbook is being independently redesigned and will be included in a future release.

The original institutional workbook is not included in this repository.

Methodology

Markowitz Optimization

The application uses mean-variance optimization to identify portfolios that minimize risk for different target returns.

Portfolio variance is calculated as:

Portfolio Variance = wᵀΣw

where:

* w is the vector of portfolio weights;
* Σ is the variance-covariance matrix.

The resulting portfolios form the efficient frontier.

Michaud Resampling

Michaud resampling is used to reduce the sensitivity of traditional Markowitz optimization to estimation errors.

The application:

1. generates multiple simulated return scenarios;
2. performs portfolio optimization for each simulation;
3. calculates the efficient portfolios;
4. averages the optimized portfolio weights;
5. produces a more diversified resampled efficient frontier.

The default implementation runs 500 simulations.

Current Limitations

* Maximum of 18 assets
* Excel workbook structure must match the required template
* Expected returns may require manual input
* Historical results do not guarantee future performance
* The optimizer does not include transaction costs or taxation
* Short selling constraints depend on the selected model settings

Planned Improvements

* Redesigned Excel input template
* Improved error handling
* More flexible number of assets
* Additional portfolio risk metrics
* Interactive charts
* Improved graphical interface
* Automatic market data import
* Portfolio performance reporting

Disclaimer

This project is intended exclusively for educational and research purposes.

It does not constitute investment advice, financial advice or a recommendation to buy or sell any financial instrument.

Portfolio optimization results depend on assumptions, historical data and estimated returns. Actual investment results may differ significantly.

Author
Alessio Bisceglia

License

This project is distributed under the MIT License.

See the LICENSE file for further information.
