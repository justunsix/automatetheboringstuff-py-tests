# About:
# Test Network Connections in an OpenShift project's pod
# with a specified destination IP and port
# Usage Example:
# python k8s-oc-test-pod-connections.py openshift_project_name csv_file_path

# Requires openshift-client installed per https://github.com/openshift/openshift-client-python
import csv
import openshift as oc
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Test Network Connections in an OpenShift project\'s pod with a set of destination IPs and ports.')
# Add an argument for the project name
parser.add_argument('project_name', help='The name of the OpenShift project to test connections in')
# Add an argument for the CSV file path
parser.add_argument('csv_file_path', help='The path to the CSV file with rows destination_ip and destination_port to test connections to')
# Parse the arguments
args = parser.parse_args()

OC_PROJECT_SELECTED = args.project_name
CSV_FILE_PATH = args.csv_file_path

def read_destinations_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Set a project context for all inner `oc` invocations and limit execution to 30 seconds
with (oc.project(OC_PROJECT_SELECTED), oc.timeout(30)):
    result_oc_project = oc.invoke('project')
    print(result_oc_project.out)

    # Print the list of qualified pod names (e.g. ['pod/xyz', 'pod/abc', ...]  in the current project
    print('Found the following pods in project {}: {}'.format(oc.get_project_name(), oc.selector('pods').qnames()))

    # Read in the current state of the pod resources and represent them as python objects
    for pod_obj in oc.selector('pods').objects():
        
        # The APIObject class exposes several convenience methods for interacting with objects
        print('================================================\n'
              'Analyzing pod: {}'.format(pod_obj.name()))
        result_date = pod_obj.execute(['date'])
        print(f'Date (UTC): {result_date.out()}')

        destinations = read_destinations_from_csv(CSV_FILE_PATH)
        for row in destinations:
            destination_ip = row['destination_ip']
            destination_port = row['destination_port']
            
            # Show row information, useful if there is information about the destination in other columns of the csv file
            print(f"----------------------\nDestination Information: {row}")                
            nc_command = f'nc -zv {destination_ip} {destination_port}'

            try: 
                result_nc = pod_obj.execute(['nc', '-zv', destination_ip, destination_port])
                if 'Connected' in result_nc.err():
                    print(f"\033[92m✓ Connection was successful from pod running {nc_command}\033[0m")
                    print(f"nc output: {result_nc.err()}")
            except Exception as e:
                print(f"\033[91mX Connection was NOT successful from pod running {nc_command}:\033[0m")
                # Error details 
                # print(e)