FROM jenkins/jenkins:lts

# CVE-2024-23897 — Arbitrary File Read via CLI
# Also: Script Console with weak creds

ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Install plugins needed for exploitation
RUN jenkins-plugin-cli --plugins \
    configuration-as-code \
    git \
    workflow-aggregator \
    credentials \
    credentials-binding

# JCasC with weak creds and stored secrets
COPY jenkins.yaml /var/jenkins_home/casc.yaml
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yaml

# Flag
USER root
RUN echo "FLAG{j3nk1ns_cl1_f1l3_r3ad}" > /flag.txt && chmod 644 /flag.txt
USER jenkins
