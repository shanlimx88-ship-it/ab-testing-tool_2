cat > README.md << 'EOF'
# Skill 3.2: Experiment Analysis & Multiple Comparison Correction

## Overview
Analyze A/B test results with proper statistical methods. Handle multiple metrics with multiple comparison correction to control false positive rate.

## Features
- **Metric Analysis**: Support proportion metrics (retention, conversion) and continuous metrics (sessions, latency)
- **Statistical Tests**: Z-test for proportions, T-test for continuous metrics
- **Multiple Comparison Correction**: Bonferroni, Holm, FDR (Benjamini-Hochberg)
- **Guardrail Check**: Automatically detect metric degradation
- **Confidence Intervals**: Bootstrap-based 95% CI for lift
- **HTML Report**: Self-contained report with results table and charts

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate sample data
python run_analysis.py --generate-sample

# Run analysis
python run_analysis.py --data data/sample_experiment_data.csv
