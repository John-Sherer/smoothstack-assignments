import logging
import os
import matplotlib.pyplot as plt
import pandas as pd


# Helper function for validating phone numbers
def validate_phone_numbers(db, column_name):
    result = 0
    for phone_number in db[column_name]:
        if len(phone_number.strip()) == 0:
            continue
        subset = phone_number.split('.')
        if len(subset) != 3:
            logging.warning("Warning, detected an invalid phone number in Agent Phone Numbers: " + phone_number)
            continue
        try:
            if not (int(subset[0]) < 1000 and int(subset[1]) < 1000 and int(subset[2]) < 10000 and
                    len(subset[0]) == 3 and len(subset[1]) == 3 and len(subset[2]) == 4):
                logging.warning("Warning, detected an invalid phone number in Agent Phone Numbers: " + phone_number)
        except ValueError:
            logging.warning("Warning, detected an invalid phone number in Agency Phone Numbers: " + phone_number)
            continue
        result += 1
    return result


if __name__ == '__main__':
    # For validation purposes
    valid_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',
                    'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
                    'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
                    'WV', 'WI', 'WY']

    # Load the logger
    logging.basicConfig(filename='logfile.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')

    # Get files in the current directory and sort by date
    files = [file for file in os.listdir(os.getcwd()) if file[:15] == 'NYL_FieldAgent_' and file[-4:] == '.csv']
    files = sorted(files, key= lambda string: int(string[15:23]))
    logging.info("Identified {len(files)} files, sorted by date:")
    for file in files:
        logging.info("\t" + file)

    # Open two most recent files for comparison, and check for disparity in row count
    recent_file = pd.read_csv(files[0])
    older_file = pd.read_csv(files[1])
    recent_lines = len(recent_file)
    older_lines = len(older_file)

    if abs(recent_lines - older_lines) > 500:
        logging.warning("Warning, discrepancy between most recent files is too large to continue " +
                     "({} lines vs {} lines).".format(recent_lines, older_lines))
        exit(1)
    logging.info("Both files are within acceptable length difference ({} lines vs {} lines).".format(recent_lines,
                                                                                                     older_lines))

    # Check that this file has not already been processed
    processed_file_list = open('NYL.lst', 'r')
    if processed_file_list.read().find(files[0]) != -1:
        logging.warning("Warning, this file has already been processed. Exiting.")
        exit(1)

    # Write file to list for future reference
    logging.info("File has not yet been processed, according to NYL.lst. Appending to list.")
    processed_file_list = open('NYL.lst', 'a')
    processed_file_list.write(files[0] + '\n')

    # Rename columns if necessary
    recent_file.rename(inplace=True, columns={'Agent Writing Contract Start Date (Carrier appointment start date)':
                                              'Agent Writing Contract Start Date',
                                              'Agent Writing Contract Status (actually active and cancelled\'s '
                                              'should come in two different files)': 'Agent Writing Contract Status'})

    # Validate phone numbers
    logging.info("Validating Agency Phone Numbers.")
    valid_count = validate_phone_numbers(recent_file, 'Agency Phone Number')
    logging.info("Identified {} valid phone numbers.".format(valid_count))
    logging.info("Validating Agent Phone Numbers.")
    valid_count = validate_phone_numbers(recent_file, 'Agent Phone Number')
    logging.info("Identified {} valid phone numbers.".format(valid_count))

    # Validate states
    logging.info("Validating Agent States.")
    valid_count = 0
    for state in recent_file['Agent State']:
        if state in valid_states:
            valid_count += 1
        else:
            logging.warning("Warning, detected invalid state abbreviation: " + state)
    logging.info("Identified {} valid states.".format(valid_count))

    # Validate emails
    logging.info("Validating email addresses.")
    valid_count = 0
    for email in recent_file['Agent Email Address']:
        if email[-19:].lower() == '@ft.newyorklife.com' and len(email) >= 20:
            valid_count += 1
        else:
            # Check if the email is unusual, or just invalid
            if email.find('@') != -1 and len(email[:email.find('@')]) > 1 and \
                    len(email[email.find('@')+1:]) > 1 and email[email.find('@')+1:].find('.') != -1:
                logging.warning("Warning, detected unusual email address: " + email)
            else:
                logging.warning("Warning, detected invalid email address: " + email)
    logging.info("Identified {} valid email addresses.".format(valid_count))

    # Display the data frame
    logging.info("Printing file info to console.")
    recent_file.info()
    print(recent_file.head(20))

    # Creating a dataframe of agents grouped by state
    logging.info("Creating dataframe for agents grouped by state")
    agents_by_state = recent_file.groupby('Agent State').size()
    print(agents_by_state.head(20))

    # Creating abbreviated dataframe with select columns
    logging.info("Creating dataframe for only agent names, contract dates and A20 dates.")
    abbreviated_agents = recent_file[['Agent Last Name', 'Agent Middle Name', 'Agent First Name',
                                      'Agent Writing Contract Start Date', 'Date when an agent became A2O']]
    print(abbreviated_agents.head(20))

    logging.info("Creating histogram")

    # Prevent histogram from printing excessively to the log file
    logging.setLevel(40)
    histogram = agents_by_state.plot.bar()
    histogram.plot()

    plt.show()
