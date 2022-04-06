export default {   
    UPLIT_API: {
      //URL: `${process.env.REACT_APP_HOST_PROTOCOL}://${process.env.REACT_APP_HOST_ADDRESS}/api/v1/`,
      URL: "http://18.118.105.254/api/v1/",
      RESOURCES: {
        SELLER: "account/sellers/",
        VIRTUALSHOP: "virtual-shops/",
        VIRTUALSHOP_LIST_CATEGORIES: "virtual-shops/<id>/food-items-categories/",
        FOOD_ITEM_CATEGORY: "food-items-categories/",
        IMAGE: "images/",
        FOOD_ITEMS: "food-items/",
        TAGS: "tags-food-items/"
      }
    },
    UPLIT_AUTHENTICATION: {
      //URL: `${process.env.REACT_APP_HOST_PROTOCOL}://${process.env.REACT_APP_HOST_ADDRESS}/`,
      URL: "http://18.118.105.254/",
      RESOURCES: {
        TOKEN: "auth/token/"
      }
    }
}