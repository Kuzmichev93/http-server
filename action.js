
let value_enter = document.querySelector('.input_enter');
let value_out = document.querySelector('.input_out');

let error = document.querySelector('.error');
async function resp(arg){
    let res;
    let url = 'http://localhost:8060/decod';
    let parametrs = {"key":"param",'param':arg}
    await fetch(url,{method: "post",
                       headers:{"Content-Type":"application/json"},
                       body:JSON.stringify(parametrs)}).then((response)=>{return response.text()})
                       .then((data)=>{res=data});
   return res;
}
async function test(){

  let regular_value_all;
  let enter_input=value_enter.value.replace(/\./ig,'').length;
  let regular = value_enter.value.match(/[0-9a-z.?]{3}/ig)

  try{
     if (regular.join("").replace(/\./ig,'').length>3){
         regular_value_all = regular.join("").replace(/\./ig,'').length;
         console.log(regular_value_all)

         }
       else{
           regular_value_all = regular[0].replace(/\./ig,'').length;


       }
  }
  catch{}

  if (regular_value_all == enter_input){
     value_out.value = await resp(regular);

  }
  else{
    error.style.display = 'block';
  }
}

function action(){
   let last_name;
   document.body.addEventListener("click",(e)=>{
   let name = e.target.className

   if(name == "input_enter"){
        last_name=e.target;
        error.style.display='none';
        value_enter.style.color='black';
        if(last_name.value=="A3.85.A2.A3."){
        e.target.value='';
        e.target.addEventListener("mouseout",()=>{
        if(last_name.value=='')
        {last_name.value="A3.85.A2.A3.";
         value_enter.style.color='darkgray';
        }
        e.target.addEventListener("keydown",()=>{
        if(last_name.value=="A3.85.A2.A3.")
            {last_name.value='';
             value_enter.style.color='black';
             }})
        })}


   }
   else{
     if(last_name.value==''){
     last_name.value="A3.85.A2.A3.";}
   }

   })


}

action();