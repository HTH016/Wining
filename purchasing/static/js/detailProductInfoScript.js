const qnty = document.getElementById("qnty");
const btnBuy = document.getElementById("btnBuy")
const sellId = document.getElementById("sellId")
const sellForm = document.getElementById("sellForm");

qnty.addEventListener("change", priceCalc);
btnBuy.addEventListener("click", buyListLocation);
sellForm.addEventListener("submit", checkLogin);				
					
function priceCalc(){
	document.getElementById("purchasePrice").value 
		= document.getElementById("qnty").value * document.getElementById("sellPrice").value;
}


function buyListLocation(){
	link = "../payment?sellid=" + sellId.value + "&qnty=" + document.getElementById("qnty").value;
	location.href = link;
}

function checkLogin(event){
	if (document.getElementById("userId").value == "None"){
		const doLogin = confirm("��ٱ��Ͽ� �ش� ��ǰ�� �߰��Ͻ÷��� �α��� �ϼž� �մϴ� \n �α��� �Ͻðڽ��ϱ�?")
		console.log(doLogin);
		if (doLogin == false){
			event.preventDefault();
			return false;
		}

		else if(doLogin==true){
			event.preventDefault();
			window.open("../templogin", "_black", "width=500, height=700");
			return false;
		}
		
	}
}
