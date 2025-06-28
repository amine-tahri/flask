import axios from 'axios'
async function f() {
  try {
    // const response = await axios.post('http://127.0.0.1:5000/login',{ name: 'amine', password: '123456' },{headers: { 'No-Authorization': true }},)
    const response = await axios.post('http://127.0.0.1:5000/refresh',{},{headers: { 'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NTQ0NzgyOCwianRpIjoiYTA4NTEwOTMtYTE1Ny00NTc5LTk5OTctNTA1MGRlNjdjNmUwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJhbWluZSIsIm5iZiI6MTc0NTQ0NzgyOCwiY3NyZiI6IjhkM2NmNzQ3LTVhZDQtNDRmNy1hZTM2LWM1ODIzYTc4ZTI4YiIsImV4cCI6MTc0ODAzOTgyOH0.Pf71uJMnF-ktZkyb6CCkfEhIHgnP_WFwBcVzpf0S66I" }},)
    console.log(response.data)
  } catch (error) {
    console.log(error)
  }
}
f()

// {
//     access_token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NTQ0NzQ3MiwianRpIjoiMTJlOGMzYTItN2I3Zi00ZDNjLTk0YWUtNDBhYWY1OWI3N2NhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFtaW5lIiwibmJmIjoxNzQ1NDQ3NDcyLCJjc3JmIjoiMjJmZmU3MzEtYTA0Ny00OTQ2LWE5ZjEtNGE5Njc5ODlhYWU4IiwiZXhwIjoxNzQ1NDQ3NTAyfQ.TKBV4YtVvOPY3anZAz3vDfC9ra92Ay9dwuRxqJZRNX8',
//     refresh_token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NTQ0NzQ3MiwianRpIjoiMzUxZjBhNjktNGI2OC00NmU3LWJhNzQtMDE1ZDVlMzQxOTkxIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJhbWluZSIsIm5iZiI6MTc0NTQ0NzQ3MiwiY3NyZiI6ImE4NTUyZjQ1LTFhNjQtNDQ5Ni04NGJjLTAxZWZiYTJhOWQ5OSIsImV4cCI6MTc0ODAzOTQ3Mn0.9jtEMl-uPywyNJQIwLkwJlkhyEEUcauM6mpCWoqaiO4',
//     user_details: { address: 'TN', id: 1, name: 'amine' }
//   }
