# Setup dependencies
poetry export -f requirements.txt --output requirements.txt

# Deploy app to vercel production
vercel --prod