npm install
npm run dev

az login
az webapp up --name roda-ai-app --runtime "NODE|18-lts" --sku F1

npm run build
npm run deploy

npm install --save-dev gh-pages
