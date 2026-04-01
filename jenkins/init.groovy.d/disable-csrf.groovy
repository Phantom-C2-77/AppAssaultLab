import jenkins.model.Jenkins

// Disable CSRF protection (intentional vulnerability for lab)
def instance = Jenkins.getInstance()
instance.setCrumbIssuer(null)
instance.save()
