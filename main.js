var swiper = new Swiper(".mySwiper", {
    loop: true,
    navigation: {
        nextEl: "#next",
        prevEl: "#prev",
    },
});

const hamburger = document.querySelector('.hamburger');
const bars = document.querySelector('.fa-bars');
const mobileMenu = document.querySelector('.mobile-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        mobileMenu.classList.toggle('mobile-menu-active');
        bars.classList.toggle('fa-xmark'); 
    });
}

let productlist = [];
let cartProduct = [];

const popularBox = document.querySelector('.popular-box');
const cartlist = document.querySelector('.cart-list');
const cartTotal = document.querySelector('.cart-total');
const cartValue = document.querySelector('.cart-value');

const updateTotal = () => {

    let totalPrice = 0;
    let totalQuantity = 0;

    document.querySelectorAll('.item').forEach(item => {
        const quantity = parseInt(item.querySelector('.quantity-value').textContent);
        const price = parseFloat(item.querySelector('.item-total').textContent.replace('$', ''));

        totalQuantity += quantity;
        totalPrice += price;
    });

    cartTotal.textContent = `$${totalPrice.toFixed(2)}`;
    cartValue.textContent = totalQuantity;
};

const showPopular = () => {
    popularBox.innerHTML = "";

    productlist.forEach(product => {

        const item = document.createElement('div');
        item.classList.add('popular-card');

        item.innerHTML = `
            <div class="card-image">
                <img src="${product.image}" alt="${product.name}">
            </div>
            <h4>${product.name}</h4>
            <h4 class="price">${product.price}</h4>
            <button class="btn card-btn" data-id="${product.id}">Add to Cart</button>
        `;

        popularBox.appendChild(item);

        item.querySelector('.card-btn').addEventListener('click', (e) => {
            e.preventDefault();
            addToCard(product);
        });
    });
};

const addToCard = (product) => {

    const existingProduct = cartProduct.find(item => item.id == product.id);

    if (existingProduct) {
        alert("Item already in your cart!");
        return;
    }

    cartProduct.push(product);

    let quantity = 1;
    let price = parseFloat(product.price.replace('$', ''));

    const cartItem = document.createElement('div');
    cartItem.classList.add('item');

    cartItem.innerHTML = `
        <div class="item-image">
            <img src="${product.image}">
        </div>
        <div class="detail">
            <h4>${product.name}</h4>
            <h4 class="item-total">$${price.toFixed(2)}</h4>
        </div>
        <div class="flex">
            <a href="#" class="quantity-btn minus">
                <i class="fa-solid fa-minus"></i>
            </a>
            <h4 class="quantity-value">${quantity}</h4>
            <a href="#" class="quantity-btn plus">
                <i class="fa-regular fa-plus"></i>
            </a>
        </div>
    `;

    cartlist.appendChild(cartItem);
    updateTotal();

    const plusBtn = cartItem.querySelector('.plus');
    const minusBtn = cartItem.querySelector('.minus');
    const quantityValue = cartItem.querySelector('.quantity-value');
    const itemTotal = cartItem.querySelector('.item-total');

    // ----- PLUS -----
    plusBtn.addEventListener('click', (e) => {
        e.preventDefault();
        quantity++;
        quantityValue.textContent = quantity;
        itemTotal.textContent = `$${(price * quantity).toFixed(2)}`;
        updateTotal();
    });

    // ----- MINUS -----
    minusBtn.addEventListener('click', (e) => {
        e.preventDefault();
        quantity--;

        if (quantity < 1) {
            cartItem.classList.add('slide-out');

            setTimeout(() => {
                cartItem.remove();
                cartProduct = cartProduct.filter(item => item.id !== product.id);
                updateTotal();
            }, 300);

            return;
        }

        quantityValue.textContent = quantity;
        itemTotal.textContent = `$${(price * quantity).toFixed(2)}`;
        updateTotal();
    });
};

// ----- INIT ----- 
const initApp = () => {
    fetch('products.json')
        .then(response => response.json())
        .then(data => {
            productlist = data;
            showPopular();
        });
};

initApp();

// ----- CART TAB -----
const cartIcon = document.querySelector('.cart-icon');
const cartTab = document.querySelector('.cart-tab');
const closeBtn = document.querySelector('.close-btn');

cartIcon.addEventListener('click', () => {
    cartTab.classList.add('cart-tab-active');
});

closeBtn.addEventListener('click', () => {
    cartTab.classList.remove('cart-tab-active');
});

const signinBtn = document.querySelector('.signin-btn');
const signinModal = document.querySelector('.signin-modal');
const closeSignin = document.querySelector('.close-signin');
const loginBtn = document.querySelector('#loginBtn');
const errorBox = document.querySelector('.signin-error');

signinBtn.addEventListener('click', e => {
    e.preventDefault(); // empêche le lien #
    signinModal.classList.add('signin-modal-active');
});

closeSignin.addEventListener('click', () => {
    signinModal.classList.remove('signin-modal-active');
});

// Login fake
loginBtn.addEventListener('click', () => {
    const email = document.querySelector('#email').value.trim();
    const password = document.querySelector('#password').value.trim();

    if(email === "" || password === ""){
        errorBox.textContent = "Please fill all fields!";
        return;
    }

    if(email === "admin@gmail.com" && password === "1234567891"){
        errorBox.style.color = "green";
        errorBox.textContent = "Login successful!";
        setTimeout(() => signinModal.classList.remove('signin-modal-active'), 800);
    } else {
        errorBox.style.color = "red";
        errorBox.textContent = "Invalid email or password!";
    }
});
