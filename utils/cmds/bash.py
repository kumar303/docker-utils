import os


def bash(config, project):
    project = config.get_project(project.project)
    cmd = ('docker exec -t -i {0} /bin/bash'
           .format(config.get_container(project).id))
    os.system(cmd)
    return
