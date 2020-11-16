<template>
  <div >
    <table>
      <thead>
      <tr>
        <th>Vendor</th>
        <th>Model</th>
        <th>Year</th>
        <th>Volume</th>
        <th>Remove</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="car in cars" v-bind:key="car.id">
          <td>{{ car.vendor }}</td>
          <td>{{ car.model }}</td>
          <td>{{ car.year }}</td>
          <td>{{ car.volume }}</td>
          <td><button @click="removeCar(car)">-</button></td>
      </tr>
      </tbody>
    </table>

    <input placeholder="vendor" v-model="currentCar.vendor">
    <input placeholder="model" v-model="currentCar.model">
    <input placeholder="year" v-model.number="currentCar.year">
    <input placeholder="volume" v-model.number="currentCar.volume">
    <button @click="createCar()">Create</button>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      cars: [],
      currentCar: {},
    };
  },
  async created() {
    // eslint-disable-next-line no-unused-vars
    this.fetchCars();
  },
  methods: {
    async fetchCars() {
      const response = await fetch(`http://127.0.0.1:8000/api/cars/`);
      this.cars = await response.json();
    },
    async createCar() {
      const response = await fetch(`http://127.0.0.1:8000/api/cars/`,
        {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.currentCar),
        });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCars();
    },
    async removeCar(car) {
      const { id } = car;
      const response = await fetch(`http://127.0.0.1:8000/api/cars/${id}/`,
        {
          method: 'DELETE',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
          },
        });
      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCars();
    },

  },
};
</script>
