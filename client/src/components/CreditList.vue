<template>
  <div class='creditList'>
    <span v-bind:class="{ hidden: selected == 1 }">
      <b-icon
        icon="arrow-left-circle-fill"
        font-scale="2"
        class="left"
        v-on:click="pre"
      ></b-icon>
    </span>
    <div
      class="imgList"
      v-bind:style="{
        transform: 'translate(-' + (selected - 1) * 690 + 'px, 0px)',
      }"
    >
      <CreditListItem
        v-for="(person, index) in credit"
        v-bind:key="index"
        v-bind:person="person"
      />
    </div>
    <span v-bind:class="{ hidden: selected == page }">
      <b-icon
        icon="arrow-right-circle-fill"
        font-scale="2"
        class="right"
        v-on:click="next"
      ></b-icon>
    </span>
  </div>
</template>

<script>
import CreditListItem from "@/components/CreditListItem.vue";
export default {
  data() {
    return {
      page: 2,
      selected: 1,
    };
  },
  props: {
    credit: Array,
  },
  components: {
    CreditListItem,
  },
  methods: {
    next() {
      if (this.selected == this.page) {
        this.selected == 1;
      } else {
        this.selected = this.selected + 1;
      }
    },
    pre() {
      if (this.selected == 1) {
        this.selected == this.page;
      } else {
        this.selected = this.selected - 1;
      }
    },
  },
};
</script>

<style scoped>
.creditList {
  position: relative;
  height: 175px;
  width: 690px;
  overflow: hidden;
  flex-direction: row;
  /* 좌우 보이게 만들고 싶으면 뺄것*/
}
.imgList {
  display: flex;
  /* overflow: hidden; */
  transition: 1s;
}
.hidden {
  visibility: hidden;
}
.right {
  position: absolute;
  right: 5px;
  top: 77%;
  z-index: 30;
  cursor: pointer;
  color: white;
}
.left {
  position: absolute;
  left: 5px;
  top: 77%;
  z-index: 30;
  cursor: pointer;
  color: white;
}
</style>
