// -*- C++ -*-
//
// Package:    MuonNumberingInitialization
// Class:      MuonNumberingInitialization
// 
/**\class MuonNumberingInitialization MuonNumberingInitialization.h Geometry/MuonNumberingInitialization/interface/MuonNumberingInitialization.h

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Michael Case
//         Created:  Thu Sep 28 16:40:29 PDT 2006
//
//

#include <memory>

#include "FWCore/Framework/interface/ModuleFactory.h"
#include "FWCore/Framework/interface/ESProducer.h"
#include "FWCore/Framework/interface/ESTransientHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DetectorDescription/Core/interface/DDFilter.h"
#include "DetectorDescription/Core/interface/DDFilteredView.h"
#include "DetectorDescription/Core/interface/DDsvalues.h"
#include "gemqc8/Geometry/interface/MuonDDDConstantsForQC8.h"
#include "Geometry/Records/interface/MuonNumberingRecord.h"

using namespace QC8;
class MuonNumberingInitializationForQC8 : public edm::ESProducer
{
public:
  
  MuonNumberingInitializationForQC8( const edm::ParameterSet& );
  ~MuonNumberingInitializationForQC8() override;

  typedef std::unique_ptr<MuonDDDConstants> ReturnType;

  ReturnType produce( const MuonNumberingRecord& );

  void initializeMuonDDDConstants( const IdealGeometryRecord& igr );

private:
  
  std::string label_;
  QC8::MuonDDDConstants* muonDDDConst_;
};

MuonNumberingInitializationForQC8::MuonNumberingInitializationForQC8( const edm::ParameterSet& iConfig )
  : muonDDDConst_( nullptr )
{
  setWhatProduced( this, dependsOn( &MuonNumberingInitializationForQC8::initializeMuonDDDConstants ));
}

MuonNumberingInitializationForQC8::~MuonNumberingInitializationForQC8()
{}

MuonNumberingInitializationForQC8::ReturnType
MuonNumberingInitializationForQC8::produce(const MuonNumberingRecord& iRecord)
{
  if ( muonDDDConst_ == nullptr )
  {
    edm::LogError( "MuonNumberingInitialization" ) << "MuonNumberingInitialization::produceMuonDDDConstants has NOT been initialized!";
    throw;
  }
  return std::unique_ptr<MuonDDDConstants> ( muonDDDConst_ ) ;
}

void
MuonNumberingInitializationForQC8::initializeMuonDDDConstants( const IdealGeometryRecord& igr )
{
  edm::ESTransientHandle<DDCompactView> pDD;
  igr.get( label_, pDD );

  if( muonDDDConst_ != nullptr ) {
    delete muonDDDConst_;
  }

  muonDDDConst_ = new MuonDDDConstants( *pDD );
}

DEFINE_FWK_EVENTSETUP_MODULE(MuonNumberingInitializationForQC8);
