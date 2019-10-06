<template>
  <div id="app">
    <img src="./assets/logo.png">
    <employee-list></employee-list>
  </div>
</template>

<script>
import EmployeeList from './components/EmployeeList'

export default {
  name: 'App',
  components: {
    EmployeeList
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
