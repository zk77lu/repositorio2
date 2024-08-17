 

function fechar(){
    var Element_x=document.getElementById("x")
    var Element_=document.getElementById('dvInfosMenu')
    Element_x.style.zIndex='-1'
    Element_.style.display="none"

}

function abrir(){
    var Element_x=document.getElementById("x")
    
    var Element_=document.getElementById('dvInfosMenu')
    Element_.style.display='block'
    Element_x.style.display='block'
    Element_x.style.zIndex='1'
   
}

// Slide fotos
document.addEventListener("DOMContentLoaded", function() {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.slide');
  
    function showSlide(index) {
      slides.forEach((slide, i) => {
        if (i === index) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });
    }
  
    function nextSlide() {
      currentIndex = (currentIndex + 1) % slides.length;
      showSlide(currentIndex);
    }
  
    // Troca de slide a cada 3 segundos (3000ms)
    setInterval(nextSlide, 5000);
  });

  
  
//   area de pesquisa de produtos
function abrirPesq(){
    var procElem = document.getElementById('sess_pesq');
    procElem.style.display='block'
}

function fecharPesq(){
    var procElem=document.getElementById('sess_pesq')
    procElem.style.display='none'
}
// Abrir/Fechar elemento/animação +
function dilatar(){
  var busq=document.getElementById('menos')
  var dilat2=document.getElementById('dv_expand2')
  var busq2=document.getElementById('menos2')
  
  var dilat=document.getElementById('dv_expand')
 
  if(dilat2.style.height=='auto'){
    dilatar2()
  }
  
  if(busq.style.transform=='rotate(90deg)'){
    
    busq.style.transform='rotate(180deg)'
    dilat.style.height='35px'

    
    
    
  }
  else{
    
    busq.style.transform='rotate(90deg)'
    dilat.style.height='auto'

    
    


  }
  

  
}
function dilatar2(){
  var busq=document.getElementById('menos2')
  var busq1=document.getElementById('menos')
  
  var dilat=document.getElementById('dv_expand2')
  var dilat1=document.getElementById('dv_expand')
  
  if(dilat1.style.height=='auto'){
    dilatar()
  }
  

  if(busq.style.transform=='rotate(90deg)'){
    busq.style.transform='rotate(180deg)'
    dilat.style.height='35px'
    
    
    
    
   
  }
  else{
    busq.style.transform='rotate(90deg)'
    dilat.style.height='auto'
    

    
    


  }
  

  
}

function salve(){
  
  localStorage.setItem('logic','sim')
  

}


function fechN(){
  var buscElement=document.getElementById('dv_super_formsPag')
  buscElement.style.height='60px'
  
}

function abrirFmPag(){
  var buscElement=document.getElementById('dv_super_formsPag')
  if(buscElement.style.height=='auto'){
    buscElement.style.height='60px'
    
  }
  else{
    buscElement.style.height='auto'
    
    setTimeout(fechN,30000)
    

  }
}





// codigo ficha tecnica, informaçoes,....
document.addEventListener('DOMContentLoaded', function () {
  var divs = document.querySelectorAll('.estru1');

  var togglerButtons = document.querySelectorAll('.buttomAbriFechar_');

  var togglerIcons = document.querySelectorAll('.estru2_txt_svg');

  togglerButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      var parentDiv = button.closest('.estru1');
      toggleSection(parentDiv);
    });
  });

  togglerIcons.forEach(function (icon) {
    icon.addEventListener('click', function () {
      var parentDiv = icon.closest('.estru1');
      toggleSection(parentDiv);
    });
  });

  function toggleSection(clickedElement) {
    var isOpen = clickedElement.classList.toggle('expanded');

    divs.forEach(function (element) {
      if (element !== clickedElement && element.classList.contains('expanded')) {
        element.classList.remove('expanded');
      }
    });

    var setinha = clickedElement.querySelector('.setinha');
    var button = clickedElement.querySelector('.buttomAbriFechar_');

    var busqVerM = document.querySelectorAll('.buttomAbriFechar_');
    busqVerM.forEach(function (x) {
      x.textContent = 'ver mais';
    });

    var busSet = document.querySelectorAll('.setinha');
    busSet.forEach(function (y) {
      y.style.transform = 'rotate(0deg)';
    });

    if (isOpen) {
      setinha.style.transform = 'rotate(45deg)';
      button.textContent = 'ver menos';
    } else {
      setinha.style.transform = 'rotate(0deg)';
    }
  }
});

// para avaliacao
function fecharDv_avali(){
  
  var busqID=document.getElementById('tty')
  addComentUser()
  busqID.style.display='none'
  

  

}
function abrir_obgd(){
  var obgd=document.querySelector('.msg_obrigado')
  obgd.style.display='block'
}

function totAvali(tot){
  localStorage.setItem('chave_totStar',tot)
}
function verificarCampos() {
var inputY = document.getElementById("inp1").value;
var textarea = document.getElementById("inp2").value;

if (inputY === "" || textarea === "") {
alert("Por favor, preencha todos os campos antes de finalizar!");


}
else{
localStorage.setItem('name_user',inputY)
localStorage.setItem('coment_user',textarea)
let limpInp1=document.getElementById('inp1')
let limpInp2=document.getElementById('inp2')
limpInp1.value = ""
limpInp2.value = ""
abrir_obgd()

setTimeout(fecharDv_avali,5000)

}
}

function fcDvOcul(){
  var tty=document.getElementById('tty')
  tty.style.display='none'
  
}

// Infos de loja
var linkDpayment= ''

var infoNumero='Esperando numero'

var infoEmail='Esperando email'

var nameD_loja='nameLoja'

var infoEmpresaRodape= nameD_loja + " Informaçoes da pagina da loja"

document.addEventListener('DOMContentLoaded', function() {
  if (document.title === 'loja') {
    
    document.title = nameD_loja;
}
  // contato
  var busqNumCont = document.querySelectorAll('.numeroContat');
  busqNumCont.forEach(function(element) {
      element.textContent = infoNumero;
  });
  // email
  var busqEmai = document.querySelectorAll('.emailContat');
  busqEmai.forEach(function(element) {
      element.textContent = infoEmail;
  });
  // infos de rodape
  var busq_infoLojaRodape=document.getElementById('infosRodape')
  busq_infoLojaRodape.textContent=infoEmpresaRodape
  
  // link para pagina de pagamento

  
// #############
});


