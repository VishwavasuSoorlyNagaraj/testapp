# Local testing
```
source venv/bin/activate
export FLASK_APP=application.py
python -m flask run
```

# Deployment

To deploy, invoke 
```
az webapp up --sku F1 -n contingencytest -l "West Europe"
```
