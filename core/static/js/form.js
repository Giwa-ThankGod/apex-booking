const form1 = document.getElementById('form1')
const form2 = document.getElementById('form2')
const form3 = document.getElementById('form3')

form1.style.display = "block"
form2.style.display = "none"
form3.style.display = "none"

const btn_form1 = document.getElementById('btn-form1')
const btn_form2 = document.getElementById('btn-form2')
const btn_form3 = document.getElementById('btn-form3')

setInterval(() => {
    const first_name = document.getElementById('id_first_name').value;
    const last_name = document.getElementById('id_last_name').value;
    const address = document.getElementById('id_address').value;
    const gender = document.getElementById('id_gender').value;
    const country = document.getElementById('id_country').value;
    const state = document.getElementById('id_state').value;
    const area_code = document.getElementById('id_area_code').value;

    const email = document.getElementById('id_email').value;
    const password = document.getElementById('id_password').value;
    const phone = document.getElementById('id_phone').value;
    const dob = document.getElementById('id_dob').value;

    if (!first_name || !last_name || !address || !gender || !country || !state || !area_code){
        btn_form1.disabled = true
    }else{
        btn_form1.disabled = false 
    }

    if (!email || !password || !phone || !dob){
        btn_form2.disabled = true
    }else{
        btn_form2.disabled = false
    }

    ;
}, 1000)






btn_form1.addEventListener('click', (e) => {
    e.preventDefault()

    form1.style.display = "none";
    form2.style.display = "block";
})

btn_form2.addEventListener('click', (e) => {
    e.preventDefault()

    form1.style.display = "none"
    form2.style.display = "none"
    form3.style.display = "block"
})

