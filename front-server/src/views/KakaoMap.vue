<template>
    <div class="container">
        <h1>Maps</h1>
        <div class="form-group">
        <select v-model="selectedBigItem" @change="updateDynamicList">
            <option v-for="item in bigList" :key="item" :value="item">
                {{ item }}
            </option>
        </select> 
        <select v-model="selectedDynamicItem" @change="selectDynamicItem">
            <option v-for="item in dynamicList" :key="item" :value="item">
                {{ item }}
            </option>  
        </select> 
        <select v-model="selectedBankItem" @change="selectBankItem">
            <option v-for="item in bankList" :key="item" :value="item">
                {{ item }}
            </option>
        </select>
        <button type='button' class='btn btn-primary' @click="moveTo">조회</button>
        </div>
        <div id="map"></div>
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.container {
  font-family: 'Nanum Gothic', sans-serif;
}
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 70vh;
    border: 2px solid black;
    border-radius: 10px;
}
.form-group {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
}
.form-group select,
.form-group button {
    margin: 0 5px;
}
#map {
    width: 750px;
    height: 500px;
}
</style>

<script>
export default {
    name: "KakaoMap",
    data() {
        return {
            map: null,
            bigList: ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '경기도', '강원도', '충청북도','충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도'],
            seoulList: ['종로구', '중구','용산구','성동구','광진구','동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구'],
            busanList: ['중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군'],
            daeguList: ['중구','동구','서구','남구','북구','수성구','달서구','달성군'],
            incheonList: ['중구','동구','미추홀구','연수구','남동구','부평구','계양구','서구','강화군','옹진군'],
            gwangjuList: ['동구','서구','남구','북구','광산구'],
            daejeonList: ['동구','중구','서구','유성구','대덕구'],
            ulsanList: ['중구','남구','동구','북구','울주군'],
            gyeonggiList: ['고양시','수원시','용인시','과천시','광명시','광주시','구리시','군포시','김포시','남양주시','동두천시','부천시','성남시','시흥시','안산시','안성시','안양시','양주시','여주시','오산시','의왕시','의정부시','이천시','파주시','평택시','포천시','하남시','화성시','가평군','양평군','연천군'],
            gangwonList: ['강릉시','동해시','삼척시','속초시','원주시','춘천시','태백시','고성군','양구군','양양군','영월군','인제군','정선군','철원군','평창군','홍청군','화천군','횡성군'],
            chungbukList: ['제천시','청주시','충주시','괴산군','단양군','보은군','영동군','옥천군','음성군','증평군','진천군'],
            chungnamList: ['계룡시','공주시','논산시','당진시','보령시','서산시','아산시','천안시','금산군','부여군','서천군','예산군','청양군','태안군','홍성군'],
            jeonbukList: ['군산시','김제시','남원시','익산시','전주시','정읍시','고창군','무주군','부안군','순창군','완주군','임실군','장수군','진안군'],
            jeonnamList: ['광양시','나주시','목포시','순천시','여수시','강진군','고흥군','곡성군','구례군','담양군','무안군','보성군','신안군','영광군','영암군','완도군','장성군','장흥군','진도군','함평군','해남군','화순군'],
            gyeongbukList: ['경산시','경주시','구미시','김천시','문경시','상주시','안동시','영주시','영천시','포항시','고령군','군위군','봉화군','성주군','영덕군','영양군','예천군','울릉군','울진군','의성군','청도군','청송군','칠곡군'],
            gyeongnamList: ['창원시','거제시','김해시','밀양시','사천시','양산시','진주시','통영시','거창군','고성군','남해군','산청군','의령군','창녕군','하동군','함안군','함양군','합천군'],
            jejuList: ['서귀포시','제주시'],
            bankList: ['국민은행','하나은행','신한은행','우리은행','농협','기업은행'],
            dynamicList: [],
            markers: [],
            selectedBigItem: null,
            selectedDynamicItem: null,
            selectedBankItem: null,
        };
    },
    created() {
        this.loadKakaoMapScript();
    },
    methods: {
        loadKakaoMapScript() {
            if (!window.kakao) {
                const script = document.createElement("script");
                script.onload = () => {
                    kakao.maps.load(() => {
                        this.initializeMap();
                    });
                };
                script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=613f7fede859b5ed71f1259496bc432f&libraries=services&autoload=false`;
                document.head.appendChild(script);
            } else {
                this.initializeMap();
            }
        },
        initializeMap() {
            const container = document.getElementById("map");
            const options = {
                center: new kakao.maps.LatLng(37.5665, 126.9780),
                level: 5,
            };
            this.map = new kakao.maps.Map(container, options);
        },
        moveTo() {
            if (this.selectedDynamicItem && this.selectedBankItem) {
                const bank = this.selectedBigItem + " " + this.selectedDynamicItem + " " + this.selectedBankItem;
                const places = new kakao.maps.services.Places();
                const map = this.map
                const infowindow = new kakao.maps.InfoWindow({zIndex:1})

                infowindow.close()

                this.markers.forEach((marker) => {
                    marker.setMap(null)
                })
                this.markers.length = 0

                // 은행 위치 검색 및 마커 추가
                places.keywordSearch(bank, (data, bankStatus, pagination) => {
                if (bankStatus === kakao.maps.services.Status.OK) {
                    const bounds = new kakao.maps.LatLngBounds()

                    for (let i = 0; i < data.length; i++){
                        const marker = new kakao.maps.Marker({
                            map: map,
                            position: new kakao.maps.LatLng(data[i].y, data[i].x)
                        })
                        kakao.maps.event.addListener(marker, 'click', function() {
                            if (infowindow.getMap()) {
                                infowindow.close();
                                } else {
                                infowindow.setContent('<div style="padding:5px;font-size:12px;">' + data[i].place_name + "</div>");
                                infowindow.open(map, marker);
                            }
                        })
                        this.markers.push(marker)
                        bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x))
                    }
                    if (bounds && map) {
                        map.setBounds(bounds);
                    }
                } else {
                    console.error("은행 위치 검색 실패:", bankStatus);
                }
                });                
            }
        },
        updateDynamicList() {
            if (this.selectedBigItem === "서울특별시") {
                this.dynamicList = this.seoulList;
            } else if (this.selectedBigItem === "부산광역시") {
                this.dynamicList = this.busanList;
            } else if (this.selectedBigItem === "대구광역시") {
                this.dynamicList = this.daeguList;
            } else if (this.selectedBigItem === "인천광역시") {
                this.dynamicList = this.incheonList;
            } else if (this.selectedBigItem === "광주광역시") {
                this.dynamicList = this.gwangjuList;
            } else if (this.selectedBigItem === "대전광역시") {
                this.dynamicList = this.daejeonList;
            } else if (this.selectedBigItem === "울산광역시") {
                this.dynamicList = this.ulsanList;
            } else if (this.selectedBigItem === "경기도") {
                this.dynamicList = this.gyeonggiList;
            } else if (this.selectedBigItem === "강원도") {
                this.dynamicList = this.gangwonList;
            } else if (this.selectedBigItem === "충청북도") {
                this.dynamicList = this.chungbukList;
            } else if (this.selectedBigItem === "충청남도") {
                this.dynamicList = this.chungnamList;
            } else if (this.selectedBigItem === "전라북도") {
                this.dynamicList = this.jeonbukList;
            } else if (this.selectedBigItem === "전라남도") {
                this.dynamicList = this.jeonnamList;
            } else if (this.selectedBigItem === "경상북도") {
                this.dynamicList = this.gyeongbukList;
            } else if (this.selectedBigItem === "경상남도") {
                this.dynamicList = this.gyeongnamList;
            } else if (this.selectedBigItem === "제주도") {
                this.dynamicList = this.jejuList;
            }
            this.selectedDynamicItem = null;
        },
        selectDynamicItem() {
            console.log(this.selectedDynamicItem);
        },
        selectBankItem() {
            console.log(this.selectedBankItem);
        },
    },
}
</script>
