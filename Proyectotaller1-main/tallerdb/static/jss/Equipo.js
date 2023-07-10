document.getElementById('weather-form').addEventListener('submit', function(e) {
  e.preventDefault();

  var city = document.getElementById('city-input').value;

  // Realizar la solicitud a la API de OpenWeatherMap para obtener datos del clima
  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=API_KEY&units=metric`)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      mostrarInfoClima(data);
    })
    .catch(function(error) {
      console.log('Error:', error);
    });
});

function mostrarInfoClima(data) {
  var weatherInfoDiv = document.getElementById('weather-info');
  weatherInfoDiv.innerHTML = '';

  if (data.cod === 200) {
    var city = data.name;
    var temperature = data.main.temp;
    var description = data.weather[0].description;

    var weatherInfo = document.createElement('div');
    weatherInfo.innerHTML = `
      <h2>${city}</h2>
      <p>Temperatura: ${temperature}°C</p>
      <p>Descripción: ${description}</p>
    `;

    weatherInfoDiv.appendChild(weatherInfo);
  } else {
    weatherInfoDiv.innerHTML = '<p>No se encontraron datos de clima para esta ciudad.</p>';
  }
}