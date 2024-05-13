import pymc3 as pm
import numpy as np

# Generate synthetic data for demonstration
np.random.seed(0)
n_samples = 1000
age = np.random.normal(50, 10, size=n_samples)
cholesterol = np.random.normal(200, 20, size=n_samples)
hypertension = np.random.binomial(1, 0.3, size=n_samples)

# Define Bayesian model using PyMC3
with pm.Model() as medical_diagnosis_model:
    # Prior distributions for patient features
    age_prior = pm.Normal('age_prior', mu=50, sd=10)
    cholesterol_prior = pm.Normal('cholesterol_prior', mu=200, sd=20)
    hypertension_prior = pm.Bernoulli('hypertension_prior', p=0.3)
    
    # Likelihood of heart disease based on patient features
    heart_disease_prob = pm.Deterministic('heart_disease_prob',
                                          pm.math.sigmoid(0.1 * age_prior + 0.05 * cholesterol_prior + 1.0 * hypertension_prior))
    
    # Binary outcome representing heart disease
    heart_disease = pm.Bernoulli('heart_disease', p=heart_disease_prob, observed=np.random.binomial(1, heart_disease_prob))

    # Perform Bayesian inference
    trace = pm.sample(1000, tune=1000)

# Print summary of posterior distributions
print(pm.summary(trace))

# Extract posterior probabilities of heart disease
posterior_probs = trace['heart_disease_prob']

# Calculate mean and uncertainty interval (e.g., 95% credible interval)
mean_prob = np.mean(posterior_probs)
credible_interval = np.percentile(posterior_probs, [2.5, 97.5])

print(f"Estimated probability of heart disease: {mean_prob:.2f}")
print(f"95% Credible Interval: [{credible_interval[0]:.2f}, {credible_interval[1]:.2f}]")
