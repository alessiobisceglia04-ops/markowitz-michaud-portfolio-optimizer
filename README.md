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



Requirements

Before running the application, make sure Python 3 is installed.

The required Python libraries are listed in:

requirements.txt

Installation

## Run on macOS

Download the repository as a ZIP file and extract it on the Desktop.

Open Terminal and run these two commands separately:

```bash
cd ~/Desktop/"Ottimizzatore app"
```

```bash
python3 app1.py
```

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
