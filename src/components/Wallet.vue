<template>
  <section class="wallet">
    <h2>🔐 My Wallet</h2>
    <p>Your address: <strong>{{ walletAddress }}</strong></p>
    <button @click="connectWallet">Connect Wallet</button>
    <p v-if="balance !== null">Balance: {{ balance }} FDAK</p>
  </section>
</template>

<script setup>
import { ref } from 'vue'
const walletAddress = ref('Not connected')
const balance = ref(null)
function connectWallet() {
  walletAddress.value = '0xRODA1234...ABCD'
  balance.value = '1000000'
}
</script>

<style scoped>
.wallet {
  background: #111;
  padding: 2rem;
  border: 1px solid #333;
  border-radius: 8px;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background: #00ffd0;
  border: none;
  color: black;
  font-weight: bold;
  cursor: pointer;
}
</style>