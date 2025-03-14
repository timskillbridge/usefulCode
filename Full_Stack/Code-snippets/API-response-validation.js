
//Validate if an API call was successful
const validateResponse = async (argument_if_applicable) => {

  let {data} = await axios.get(`desired url here/${argument_if_applicable}/`)
  data['response'] = await axios.get(` desired url here/${argument_if_applicable}/`, {validateStatus: () => true,});
  console.log(data)
  if(data.response.status == 200) {
    // alert("worked");
    navigate(`/nav page here/${argument_if_applicable}`)
  } else {
    alert("Data wasn't retrieved")
  }
  }