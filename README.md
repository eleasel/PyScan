# PyScan: Multi-threaded Port Scanner

PyScan is a multi-threaded port scanning tool implemented in Python. It allows you to scan for open ports on a target host or IP address within specified port ranges. The script utilizes concurrent scanning techniques to improve the scanning speed and efficiency.

## Features

- Multi-threaded scanning: Concurrently scan multiple ports using multi-threading for faster results.
- Service identification: Retrieve and display the associated service or protocol for each open port.
- Customizable port ranges: Specify port ranges to scan according to your needs.
- Simple and easy-to-use: Run the script with minimal setup and get results quickly.

## Installation

1. Ensure you have Python 3.x installed on your system.

2. Clone the repository or download the `PortScan.py` script to your local machine.

3. Install the required dependencies by running the command: `pip install -r requirements.txt`

## Usage

1. Open the `port_scanner.py` script in a text editor.

2. Modify the `TARGET` and `PORT_RANGE` variables in the `main` function according to your desired target and port ranges.

3. Save the script.

4. Open a terminal or command prompt and navigate to the directory where the script is located.

5. Run the script using the command: `python port_scanner.py`

6. The script will start scanning the specified port ranges on the target and display the open ports and associated services found during the scan.

## Configuration

No additional configuration is required for basic usage. However, you may need to adjust your firewall settings to allow the scanning traffic.

## Examples

- Scan a single port range:
- Scan multiple port ranges:

## Performance Considerations

For optimal performance, consider adjusting the number of threads based on your system's capabilities. A higher number of threads may result in faster scanning, but it can also increase resource usage.

## Troubleshooting

- **Issue**: Script fails to run or throws errors related to dependencies.
**Solution**: Ensure that you have installed the required dependencies by running `pip install -r requirements.txt`.

- **Issue**: Firewall is blocking the scanning traffic.
**Solution**: Adjust your firewall settings to allow the scanning traffic or temporarily disable the firewall during the scan.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository and create your branch: `git checkout -b my-feature-branch`
2. Make your changes and test them.
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Create a new pull request.

Please ensure that your contributions adhere to the project's coding conventions and standards.

## Credits

This project uses the following open-source libraries:

- `concurrent.futures`
- `socket`

## License

This project is licensed under the [MIT License](LICENSE).



