# About:
# Test Network Connections in an OpenShift project's pod
# with a specified destination IP and port

# Requires openshift-client installed per https://github.com/openshift/openshift-client-python
import openshift as oc
import k8soctestpodconnectionsconfig as config

OC_PROJECT_SELECTED = config.OC_PROJECT_SELECTED
DESTINATIONS = config.DESTINATIONS

# print('OpenShift client version: {}'.format(oc.get_client_version()))

# Set a project context for all inner `oc` invocations and limit execution to 30 seconds
with (oc.project(OC_PROJECT_SELECTED), oc.timeout(30)):
    # Run oc project
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
        # Run network test on pod to run netcat on container
        for ip, port in DESTINATIONS.items():
            destination_ip = ip
            destination_port = port              
            # Output help
            nc_command = f'nc -zv {destination_ip} {destination_port}'
        
            try: 
                result_nc = pod_obj.execute(['nc', '-zv', destination_ip, destination_port])
                # if result_nc.err() contains string Connected, print success
                if 'Connected' in result_nc.err():
                    print(f"✓ Connection was successful from pod running {nc_command}")
                    print(f"nc output: {result_nc.err()}")
            except Exception as e:
                print(f'X Connection was NOT successful from pod running {nc_command}:')
                print(e)