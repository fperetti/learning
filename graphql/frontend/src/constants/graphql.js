import gql from 'graphql-tag'

export const ALL_EMPLOYEES_QUERY = gql`
  query AllEmployeesQuery {
    allEmployees {
    edges {
      node {
        name
        id
      }
    }
  }
  }
`
