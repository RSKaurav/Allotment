function Hostels(){
  var ls=document.getElementById("hst");
  var name=Array("Select","1.8K","1.K","12th Block","6th Block");
  Combofill1(name,ls);
}

function Blocks(){

  var ls=document.getElementById("hst");
  var ins=document.getElementById("blck");
  var B1=Array("Select","A","B");
  var B2=Array("Select","A","B","C","D");
  var B3=Array("Select","A","B","C");
  var B4=Array("Select","A","B","C","D","E");
  ins.innerHTML="";
  i=ls.selectedIndex;
  switch(i){
	case 1:
	     Combofill(B1,ins);
	     break;
	case 2:
	     Combofill(B2,ins);
	     break;
  case 3:
       Combofill(B3,ins);
       break;
  case 4:
       Combofill(B4,ins);
       break;
	default:
  }
}
function Combofill1(arr,sel){
  for(i=0;i<arr.length;i++){
    var opt=document.createElement("option");
     opt.value=i;
     opt.text=arr[i];
     sel.options.add(opt);
  }
}

function Combofill(arr,sel){
  for(i=0;i<arr.length;i++){
    var opt=document.createElement("option");
     opt.value=i+','+arr[i];
     opt.text=arr[i];
     sel.options.add(opt);
  }
}
