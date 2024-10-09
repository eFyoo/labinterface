let tg = window.Telegram.WebApp;

tg.expand();

let item = "";

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";
let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");

btn1.addEventListener("click", function () {
 if (tg.MainButton.isVisible) {
     tg.MainButton.hide();
 }
 else {
     tg.MainButton.setText("Вывести информацию по собаке Мопс");
     item = "Мопс – добрая и преданная собака для всей семьи. Таким он кажется со стороны. Такие отзывы вы получите от заводчиков. Но так ли питомец подходит хозяевам без опыта и для компании детям? Рассказываем про породу мопс с точки зрения кинологов и владельцев.";
     tg.MainButton.show();
 }
});


btn2.addEventListener("click", function () {
  if (tg.MainButton.isVisible) {
      tg.MainButton.hide();
  }
  else {
      tg.MainButton.setText("Вывести информацию по собаке Бернедудль");
      item = "'Мопс – добрая и преданная собака для всей семьи. Таким он кажется со стороны. Такие отзывы вы получите от заводчиков. Но так ли питомец подходит хозяевам без опыта и для компании детям? Рассказываем про породу мопс с точки зрения кинологов и владельцев.',";
      tg.MainButton.show();
  }
 });

 btn3.addEventListener("click", function () {
  if (tg.MainButton.isVisible) {
      tg.MainButton.hide();
  }
  else {
      tg.MainButton.setText("Вывести информацию по собаке Бассет");
      item = "'Мопс – добрая и преданная собака для всей семьи. Таким он кажется со стороны. Такие отзывы вы получите от заводчиков. Но так ли питомец подходит хозяевам без опыта и для компании детям? Рассказываем про породу мопс с точки зрения кинологов и владельцев.',";
      tg.MainButton.show();
  }
 });


 btn4.addEventListener("click", function () {
  if (tg.MainButton.isVisible) {
      tg.MainButton.hide();
  }
  else {
      tg.MainButton.setText("Вывести информацию по собаке Аффенпинчер");
      item = "'Мопс – добрая и преданная собака для всей семьи. Таким он кажется со стороны. Такие отзывы вы получите от заводчиков. Но так ли питомец подходит хозяевам без опыта и для компании детям? Рассказываем про породу мопс с точки зрения кинологов и владельцев.',";
      tg.MainButton.show();
  }
 });


Telegram.WebApp.onEvent("mainButtonClicked", function () {
 tg.sendData(JSON.stringify(item));
});

