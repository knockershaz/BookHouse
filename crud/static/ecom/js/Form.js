console.log("This is form validator")

const name = document.getElementById('name')
const phone = document.getElementById('phone')
const email = document.getElementById('email')
let username=false
let useremail=false
let userphone=false
let Success=document.getElementById('success')
Success.classList.add('d-none')
let failure=document.getElementById('failure')
failure.classList.add('d-none')


name.addEventListener('blur',()=>{
    // console.log("name listner")
    let regex=/^[a-zA-Z]([0-9a-zA-Z]){2,20}$/;
    let str = name.value;
    if(regex.test(str))
    {
        console.log("this is matched")
        name.classList.remove('is-invalid')
        username=true
    }
    else
    {
        console.log("no match")
        name.classList.add('is-invalid')
        username=false
    }
})
phone.addEventListener('blur',()=>{
    // console.log("name listner")
    let regex=/^[0-9]{10}$/;
    let str = phone.value;
    if(regex.test(str))
    {
        console.log("this is matched")
        phone.classList.remove('is-invalid')
        userphone=true
    }
    else
    {
        console.log("no match")
        phone.classList.add('is-invalid')
        userphone=false
    }
})
email.addEventListener('blur',()=>{
    // console.log("name listner")
    let regex=/^([_\-0-9a-zA-Z]+)@([_\-0-9a-zA-Z]+)\.([a-zA-Z]){2,6}$/;
    let str = email.value;
    if(regex.test(str))
    {
        console.log("this is matched")
        email.classList.remove('is-invalid')
        useremail=true
    }
    else
    {
        console.log("no match")
        email.classList.add('is-invalid')
        useremail=false
    }
})

let submit = document.getElementById('submit')
submit.addEventListener('click',(e)=>
{
    e.preventDefault();
    console.log(useremail,username,userphone)
    if(username && useremail && userphone)
    {
        Success.classList.remove('d-none')
        Success.classList.add('show')
        failure.classList.remove('show')
    }
    else{
        failure.classList.remove('d-none')
        failure.classList.add('show')
        Success.classList.remove('show')
    }
})