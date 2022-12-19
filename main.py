# This scripts is assumed to be running in a cnvrg job(e.g. workspace, experiment, etc.);
# If this is run through the local machine, login credentials must be provided for the Cnvrg authentication 

from cnvrgv2 import Cnvrg
import time

# Day in seconds
DAY = 60 * 60 * 24

# TODO
# How many days old should the experiments be to be deleted?
OLD_EXPERIMENT_AGE = DAY * 45 

def get_all_projects():
    c = Cnvrg()
    projects = c.projects.list()
    return projects

# retrieve all the experiments in all the projects
def get_all_experiments(projects: list):
    experiments = []
    for project in projects:
        experiments.append(project.experiments.list())
    
    return experiments

# extract experiments that are older than 45 days
def extract_old_experiments(experiments: list):
    current_time = time.time()

    old_experiments = []
    for experiment in experiments:
        if (experiment.end_time - current_time) > OLD_EXPERIMENT_AGE:
            old_experiments.append(experiment)

    return old_experiments

# TODO
# Delete experiments, their commits, and their artifacts
def delete_experiments(experiments: list):
    pass

def __main__():
    projects = get_all_projects()
    experiments = get_all_experiments(projects)
    old_experiments = extract_old_experiments(experiments)
    delete_experiments(old_experiments)


if __name__ == "__main__":
    __main__()