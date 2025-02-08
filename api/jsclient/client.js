const loginForm = document.getElementById('login-form')
const contentCotainer = document.getElementById('content-container')

if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    console.log(loginObjectData)
    bodyStr = JSON.stringify(loginObjectData)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options).
    then(response=>{
        console.log(response)
        return response.json()
    }
    )
    .then(handleAuthData)
    .catch(
        err=>
            console.log('err', err)
    )
}

function handleAuthData(authData){
    localStorage.setItem('acess', authData.acess)
    localStorage.setItem('refresh', authData.refresh)
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data) + "</pre>"
    }
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    }

    fetch(endpoint, options)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        writeToContent(data)
    })
    .catch(error => console.error("Error:", error))
}