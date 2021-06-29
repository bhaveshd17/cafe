const view_buttons = document.getElementsByClassName("view-button")
for(let i = 0; i<view_buttons.length; i++){
    window.addEventListener("resize", function () {
        if (window.innerWidth < 982) {
            view_buttons[i].hidden = true
        }
        else {
            view_buttons[i].hidden = false
        }
    });
    if (window.innerWidth < 982) {
        view_buttons[i].hidden = true
    }
    
}


const addCookieItem = (productId, action)=>{
    if(action === 'add'){
        if(cart[productId] === undefined){
            cart[productId] = {'quantity':1}
            // console.log(cart)
        }
        else{
            cart[productId]['quantity'] += 1
        }
    }

    if(action === 'remove'){
        cart[productId]['quantity'] -= 1
        if(cart[productId]['quantity'] <= 0){
            delete cart[productId]
        }
    }
    const d = new Date();
    d.setTime(d.getTime() + (20*24*60*60*1000));
    const expires = "expires="+ d.toUTCString();
    document.cookie = 'cart=' + JSON.stringify(cart) + "; domain=;path=/;"+expires;
    location.reload()
}




const updateUserOrder = (productId, action)=>{
    console.log('sending data...')
    const url = '/updateItem/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            productId,
            action
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
        location.reload()
    })
}

const update_cart = document.getElementsByClassName("update-cart");
console.log(update_cart)
for(let i=0 ; i < update_cart.length ;i++){
    update_cart[i].addEventListener('click', function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        if(user === 'AnonymousUser'){
            console.log('hel')
            addCookieItem(productId, action)
        }
        else{
            updateUserOrder(productId, action)
        }

    })
}