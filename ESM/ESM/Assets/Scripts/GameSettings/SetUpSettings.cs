namespace SetUp
{
    public class SetUpSettings
    {
        private RegionSettings asiaRegion;
        private RegionSettings euroRegion;
        private RegionSettings southRegion;
        private RegionSettings northRegion;
        private int database;
        public SetUpSettings(int database=0, int asia=0, int euro=0, int south=0, int north =0)
        {
            asiaRegion = (RegionSettings) asia;
            euroRegion = (RegionSettings)euro;
            southRegion = (RegionSettings)south;
            northRegion = (RegionSettings)north;
            this.database = database;
        }
        public void LoadUpSetting()
        {

        }
        public void LoadGameSetting() {
        }
    }
}
