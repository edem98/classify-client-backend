var formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

const extractData = (data) => {
  const extractedData = {};
  data.forEach((item) => {
    extractedData[item.name] = item.value;
  });
  return extractedData;
};

const getTUserCars = async (BASE_URL, data) => {
  console.log(data)
  try {
    const response = await axios.post(`${BASE_URL}users/`, {
      data: data,
    }, {
      headers: { 'X-CSRFToken': data.csrfmiddlewaretoken },
    });
    return response.data;
  } catch (errors) {
    console.error(errors);
    alert(`Could not process your request\n${errors}`);
  }
};
$('.recommanded-cars').hide();
$('#classify-form').on('submit', (e) => {
  e.preventDefault();
  const form = $('#classify-form');
  const formData = form.serializeArray();
  const BASE_URL = 'http://127.0.0.1:8000/api/';
  const extractedData = extractData(formData);
  const carsData = getTUserCars(BASE_URL, extractedData);
  carsData.then((cars) => {
    if (cars.length > 0) {
      $('#cars').empty();
      cars.forEach((item) => {
        $('#cars').append(`
          <div class="col-lg-4">
          <div class="trainer-item">
            <div class="image-thumb">
              <img width=300px height=200px src="http://127.0.0.1:8000${
                item.image
              }" alt="" />
            </div>
            <div class="down-content">
              <span>${formatter.format(item.price)} </span>
              <h4>${item.brand} ${item.model}</h4>
              <ul class="social-icons">
                <li><a href="#">View Car</a></li>
              </ul>
            </div>
          </div>
        </div>`);
      });
      $('#find-cars').fadeOut(1000);
      $('.recommanded-cars').fadeIn(1000);
    } else {
      $('#find-cars').fadeOut(1000);
      $('.recommanded-cars').fadeIn(1000);
      $('#cars').empty();
      $('#cars').append(
        '<div class="no-cars-container"><p class="no-cars">No cars available for your profile</p></div>',
      );
    }
  });
});
$('#fill-form').on('click', (e) => {
  $('.recommanded-cars').hide();
  $('#find-cars').fadeIn(1000);
});