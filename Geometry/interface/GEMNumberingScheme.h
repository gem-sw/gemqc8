#ifndef gemqc8_Geometry_GEMNumberingScheme_h
#define gemqc8_Geometry_GEMNumberingScheme_h

#include "Geometry/MuonNumbering/interface/MuonNumberingScheme.h"
#include "gemqc8/Geometry/interface/MuonDDDConstantsForQC8.h"

class MuonBaseNumber;
class DDCompactView;
class MuonDDDConstants;

class GEMNumberingScheme : public MuonNumberingScheme {

public:

  GEMNumberingScheme( const DDCompactView& cpv );
  GEMNumberingScheme( const QC8::MuonDDDConstants& muonConstants );

  ~GEMNumberingScheme() override{};
  
  int baseNumberToUnitNumber(const MuonBaseNumber&) override;
  
private:
  void initMe ( const QC8::MuonDDDConstants& muonConstants );

  int theRegionLevel;
  int theStationLevel;
  int theRingLevel;
  int theSectorLevel;
  int theRollLevel;

};

#endif
