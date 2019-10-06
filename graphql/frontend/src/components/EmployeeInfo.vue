<template>
  <div>{{employee.node.name}} ({{employee.node.id}})</div>
</template>

<script>
export default {
  name: 'EmployeeInfo',
  props: ['employee']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
