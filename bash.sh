npm install vue-router pinia ethers
# Optional (recommended):
npm install vue-toastification
npm create vite@latest roda-web4 -- --template vue
cd roda-web4
npm install

az login
az webapp up --name roda-ai-app --runtime "NODE|18-lts" --sku F1
