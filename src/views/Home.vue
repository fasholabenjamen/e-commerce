<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to E-commerce
        </p>
        <p class="subtitle">The best e-commerce store online</p>
      </div>

    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

      <ProductBox 
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import ProductBox from '@/components/ProductBox'
export default {
  name: 'Home',
  data() {
    return {
      products: []
    }
  },

  components: {
    ProductBox
  },

  mounted() {
    this.getProducts()
    document.title = 'Home | E-commerce'
  },

  methods: {
    async getProducts () { 
      this.$store.commit('setIsLoading', true)

     await axios.
      get('lastest-products')
      .then(response => {
        this.products = response.data
      })
      .catch(error => {
        console.log(error)
      })

      this.$store.commit('setIsLoading', false)
    },

  }
}
</script>

