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
		const isUser = confirm("�α��� �� ��ٱ��� ����� �̿��Ͻ� �� �ֽ��ϴ� \n �α��� �Ͻðڽ��ϱ�?")
		console.log(isUser);
		if (isUser == false){
			event.preventDefault();
			return false;
		}
		
	}
}
