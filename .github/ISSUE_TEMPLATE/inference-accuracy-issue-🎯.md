---
name: "Inference Accuracy Issue \U0001F3AF"
about: Report or discuss issues related to the accuracy of inference results
title: ''
labels: ''
assignees: ''

---

## Inference Accuracy Issue

**Describe the accuracy issue**  
A clear and concise description of the inference accuracy problem you're observing. For example, TitanML's inference stack "Takeoff" produces inconsistent results for large language models.

**Steps To Reproduce**  
Please walk us through the steps to reproduce the issue and provide the following details:
1. Load model 'GPT-3 175B'
2. Prepare input prompt "Summarize the history of AI"
3. Run inference
4. Observe inconsistent or inaccurate results

- **Packages and versions you're running:**
  - List of packages and their versions (e.g., Takeoff v0.16.0, Transformers v4.18.0)
- **Environment details:**
  - OS: (e.g., Ubuntu 20.04)
  - Python version: (e.g., Python 3.8)
  - Hardware specs: (e.g., 128GB RAM, NVIDIA A100 GPU)
- **Any deviations from the standard TitanML packages or configurations:**
  - (e.g., Custom tokenizer, Modified inference parameters)

**Expected behaviour**  
A clear and concise description of what you expected to happen. For example, the model should produce consistent and accurate summaries.

**Screenshots**  
If applicable, add screenshots or example outputs to help explain your problem.

**Additional context**  
Add any other context about the problem here. For example, this issue only occurs with models larger than 100B parameters.
