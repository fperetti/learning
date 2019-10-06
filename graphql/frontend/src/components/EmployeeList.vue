<template>
  <div>
    <employee-info
      v-for="employee in allEmployees.edges"
      :key="employee.id"
      :employee="employee">
    </employee-info>
  </div>
</template>

<script>
import EmployeeInfo from './EmployeeInfo'
import { ALL_EMPLOYEES_QUERY } from '../constants/graphql'

export default {
  name: 'EmployeeList',
  data () {
    return {
      allEmployees: []
    }
  },
  components: {
    EmployeeInfo
  },
  apollo: {
    allEmployees: {
      query: ALL_EMPLOYEES_QUERY
    }
  }
}
</script>
