const loginForm = document.getElementById('login-form')
const contentCotainer = document.getElementById('content-container')

if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}

function getFetchOptions(method, body){
    return {
        method: method === null ? 'GET' : method,
        headers: {
            "Content-Type": "application/json"
        },
        body: body ? body : null
    }
}


function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    console.log(loginObjectData)
    bodyStr = JSON.stringify(loginObjectData)
    options = getFetchOptions()
    fetch(loginEndpoint, options).
    then(response=>{
        console.log(response)
        return response.json()
    }
    )
    .then(authData=>{
        handleAuthData(authData, getProductList)
    }
    )
    .catch(
        err=>
            console.log('err', err)
    )
}


function validateJWTToken(){
    //fetch
    const endpoint = `${baseEndpoint}/token/verify`
    const options = {
        method:'POST',
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response =>response.json())
    .then(x=>{
        console.log(x)
    })
}

function handleAuthData(authData,callback){
    localStorage.setItem('acess', authData.acess)
    localStorage.setItem('refresh', authData.refresh)
    if(callback){
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data,null,4) + "</pre>"
    }
}

function  isTokenNotValid(){


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

getProductList()